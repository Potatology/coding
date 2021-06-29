 void printWord() {
    String a;
    String b;
    a ??= b ?? 'string1';
    a = b == null ? 'string2' : null;
    b ??= a;
    print(b);
  }


void main() {
  printWord();
}
