"""
Mnemonic Guard — проверяет, содержатся ли слова вашей seed-фразы в списках известных утечек.
"""

import sys
import os

LEAKS_FILE = "leaked_words.txt"

def load_leaks():
    if not os.path.exists(LEAKS_FILE):
        print(f"❌ Файл утечек {LEAKS_FILE} не найден.")
        sys.exit(1)
    with open(LEAKS_FILE, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f if line.strip())

def check_mnemonic(mnemonic_words, leaked_words):
    matches = set(mnemonic_words) & leaked_words
    if matches:
        print("⚠️ Обнаружены потенциально скомпрометированные слова:")
        for word in matches:
            print(f" - {word}")
    else:
        print("✅ Все слова seed-фразы отсутствуют в списках утечек.")

def main():
    if len(sys.argv) != 2:
        print("Использование: python mnemonic_guard.py "word1 word2 ... word12"")
        sys.exit(1)

    mnemonic_input = sys.argv[1].strip().lower().split()
    if len(mnemonic_input) not in [12, 15, 18, 21, 24]:
        print("❌ Некорректное количество слов во фразе. Должно быть 12–24.")
        sys.exit(1)

    leaked_words = load_leaks()
    check_mnemonic(mnemonic_input, leaked_words)

if __name__ == "__main__":
    main()
