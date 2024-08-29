#define A  8
#define B  7
#define C  6
#define D  5
#define E  4
#define F  3
#define G  2

#define A1  A2
#define B1  A0
#define C1  13
#define D1  12
#define E1  11
#define F1  10
#define G1  9

void setup() {
   pinMode(A, OUTPUT);
   pinMode(B, OUTPUT);
   pinMode(C, OUTPUT);
   pinMode(D, OUTPUT);
   pinMode(E, OUTPUT);
   pinMode(F, OUTPUT);
   pinMode(G, OUTPUT);

   pinMode(A1, OUTPUT);
   pinMode(B1, OUTPUT);
   pinMode(C1, OUTPUT);
   pinMode(D1, OUTPUT);
   pinMode(E1, OUTPUT);
   pinMode(F1, OUTPUT);
   pinMode(G1, OUTPUT);
  

   
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    Serial.println(command);  // Отладка: выводим команду в монитор порта

    if (command == '1') {
      digitalWrite(A, LOW);
      digitalWrite(B, LOW);
      digitalWrite(C, LOW);
      digitalWrite(D, LOW);
      digitalWrite(E, LOW);
      digitalWrite(F, LOW);
      digitalWrite(G, HIGH);
    } else if (command == '0') {
      digitalWrite(A1, LOW);
      digitalWrite(B1, LOW);
      digitalWrite(C1, LOW);
      digitalWrite(D1, LOW);
      digitalWrite(E1, LOW);
      digitalWrite(F1, LOW);
      digitalWrite(G1, HIGH);
    }
  }
  //Глазки на 2 дисплеях
   digitalWrite(A, HIGH);
   digitalWrite(B, HIGH);
   digitalWrite(C, LOW);
   digitalWrite(D, LOW);
   digitalWrite(E, LOW);
   digitalWrite(F, HIGH);
   digitalWrite(G, LOW);

   digitalWrite(A1, HIGH);
   digitalWrite(B1, HIGH);
   digitalWrite(C1, LOW);
   digitalWrite(D1, LOW);
   digitalWrite(E1, LOW);
   digitalWrite(F1, HIGH);
   digitalWrite(G1, LOW);
   delay(2000);
   //Моргает
   digitalWrite(A, LOW);
   digitalWrite(B, LOW);
   digitalWrite(C, LOW);
   digitalWrite(D, LOW);
   digitalWrite(E, LOW);
   digitalWrite(F, LOW);
   digitalWrite(G, HIGH);

   digitalWrite(A1, LOW);
   digitalWrite(B1, LOW);
   digitalWrite(C1, LOW);
   digitalWrite(D1, LOW);
   digitalWrite(E1, LOW);
   digitalWrite(F1, LOW);
   digitalWrite(G1, HIGH);
   delay(200);

  //Глазки на 2 дисплеях
   digitalWrite(A, HIGH);
   digitalWrite(B, HIGH);
   digitalWrite(C, LOW);
   digitalWrite(D, LOW);
   digitalWrite(E, LOW);
   digitalWrite(F, HIGH);
   digitalWrite(G, LOW);

   digitalWrite(A1, HIGH);
   digitalWrite(B1, HIGH);
   digitalWrite(C1, LOW);
   digitalWrite(D1, LOW);
   digitalWrite(E1, LOW);
   digitalWrite(F1, HIGH);
   digitalWrite(G1, LOW);
}
