# Mnemonic Guard

**Mnemonic Guard** — проверяет, содержатся ли слова вашей seed-фразы в офлайн-словаре утечек.

## Для чего?

Помогает проверить фразу на частичную компрометацию:
- Совпадения с утекшими seed-фразами
- Слова, использованные в популярных тестах, публикациях, демо и т.п.

## Использование

1. Убедитесь, что файл `leaked_words.txt` содержит список известных слов-утечек (в комплекте пример).
2. Запустите:

```bash
python mnemonic_guard.py "your twelve seed words here ..."
```

## Пример

```bash
python mnemonic_guard.py "apple drift moon tiger maze grape lion dog car horse correct battery"
```

## Лицензия

MIT
