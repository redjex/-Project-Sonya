#include <uspeech.h>

#define ledGreen 7
#define ledOrange 6
#define ledWhite 5
#define MIN3(a, b, c) ((a) < (b) ? ((a) < (c) ? (a) : (c)) : ((b) < (c) ? (b) : (c)))

signal voice(A0);
const int BUFFER_MAX_PHONEMES = 32;
char inputString[BUFFER_MAX_PHONEMES]; // Allocate some space for the string
byte index = 0; // Index into array; where to store the character

const int DICT_MAX_ELEMNTS = 4; // Увеличиваем размер словаря
char dict[DICT_MAX_ELEMNTS][BUFFER_MAX_PHONEMES] = {"vvvoeeeeeeeofff", "hhhhhvoovvvvf", "hooooooffffffff", "vhoooosssafff"}; // Добавляем "соня"
int LOWEST_COST_MAX_THREASHOLD = 20;

void setup() {
  voice.f_enabled = true;
  voice.minVolume = 1500;
  voice.fconstant = 500;
  voice.econstant = 2;
  voice.aconstant = 4;
  voice.vconstant = 6;
  voice.shconstant = 10;
  voice.calibrate();
  
  Serial.begin(9600);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledOrange, OUTPUT);
  pinMode(ledWhite, OUTPUT);
}

void loop() {
  voice.sample();
  char p = voice.getPhoneme();
  
  if (p == ' ' || index >= BUFFER_MAX_PHONEMES) {
    if (strLength(inputString) > 0) {
      Serial.println("received: " + String(inputString));
      parseCommand(inputString);
      inputString[0] = '\0'; // Clear string char array
      index = 0;
    }
  } else {
    inputString[index] = p; // Store it
    index++;
    inputString[index] = '\0'; // Null terminate the string
  }
}

char* guessWord(char* target) {
  int len = strlen(target); // Held target length
  static char result[BUFFER_MAX_PHONEMES];
  
  // Simple validation
  for (int i = 0; i < DICT_MAX_ELEMNTS; i++) {
    if (strcmp(dict[i], target) == 0) {
      strcpy(result, dict[i]);
      return result;
    }
  }
  
  unsigned int cost[DICT_MAX_ELEMNTS]; // Held minimum distance cost
  
  // Calculating each word's cost and hits
  for (int j = 0; j < DICT_MAX_ELEMNTS; j++) { // Loop through the dictionary
    cost[j] = levenshtein(dict[j], target);
    Serial.println("dict[j] = " + String(dict[j]) + " target = " + String(target) + " cost = " + String(cost[j]));
  }
  
  // Determining the lowest cost but still all letters in the pattern hitting word
  int lowestCostIndex = -1;
  int lowestCost = LOWEST_COST_MAX_THREASHOLD;
  
  for (int j = 0; j < DICT_MAX_ELEMNTS; j++) { // Loop through the dictionary
    if (cost[j] < lowestCost) {
      lowestCost = cost[j];
      lowestCostIndex = j;
    }
  }
  
  if (lowestCostIndex > -1) {
    strcpy(result, dict[lowestCostIndex]);
    return result;
  } else {
    strcpy(result, "");
    return result;
  }
}

void parseCommand(char* str) {
  char* gWord = guessWord(str);
  Serial.println("guessed: " + String(gWord));
  
  if (strcmp(gWord, "") == 0) {
    return;
  } else if (strcmp(gWord, dict[0]) == 0) {
    digitalWrite(ledGreen, HIGH);
    digitalWrite(ledOrange, LOW);
    digitalWrite(ledWhite, LOW);
    delay(10);
  } else if (strcmp(gWord, dict[1]) == 0) {
    digitalWrite(ledGreen, LOW);
    digitalWrite(ledOrange, HIGH);
    digitalWrite(ledWhite, LOW);
    delay(10);
  } else if (strcmp(gWord, dict[2]) == 0) {
    digitalWrite(ledGreen, LOW);
    digitalWrite(ledOrange, LOW);
    digitalWrite(ledWhite, HIGH);
    delay(10);
  } else if (strcmp(gWord, dict[3]) == 0) { // Проверяем "соня"
    Serial.println("Слово 'соня' распознано!");
    digitalWrite(ledGreen, LOW);
    digitalWrite(ledOrange, HIGH);
    digitalWrite(ledWhite, HIGH); // Включаем белый светодиод для "соня"
    delay(10);
  }
}

unsigned int levenshtein(char* s1, char* s2) {
  unsigned int s1len, s2len, x, y, lastdiag, olddiag;
  s1len = strlen(s1);
  s2len = strlen(s2);
  unsigned int column[s1len + 1];
  
  for (y = 1; y <= s1len; y++)
    column[y] = y;
  
  for (x = 1; x <= s2len; x++) {
    column[0] = x;
    for (y = 1, lastdiag = x - 1; y <= s1len; y++) {
      olddiag = column[y];
      column[y] = MIN3(column[y] + 1, column[y - 1] + 1, lastdiag + (s1[y - 1] == s2[x - 1] ? 0 : 1));
      lastdiag = olddiag;
    }
  }
  
  return column[s1len];
}

int strLength(char const* s) {
  int i = 0;
  while (s[i] != '\0' && s[i] != ' ')
    ++i;
  
  return i;
}
