# Automatizované testy s Playwrightem

Tento projekt obsahuje automatizované testy pro webové stránky pomocí knihovny **Playwright** a frameworku **pytest**.

---

## Instalace závislostí

1. Nainstalujte potřebné balíčky:
   ```bash
   pip install pytest playwright pytest-playwright

3. Nainstalujte prohlížeče pro Playwright:
   ```bash
   playwright install

---

## Spuštění testů

### Spuštění všech testů s viditelným prohlížečem
   ```bash
   venv/bin/python -m pytest --headed --slowmo 500
   ```
- --headed – spustí testy s viditelným prohlížečem  
- --slowmo 500 – zpomalí akce o 500 ms pro lepší sledování

### Spuštění testů v debug režimu
   ```bash
   PWDEBUG=1 python -m pytest
   ```
- PWDEBUG=1 – aktivuje Playwright debug mód (testy se zastaví na každé akci)

---

## Další užitečné příkazy

Rychlé spuštění testů bez zpomalení:
   ```bash
   pytest
   ```

Spuštění konkrétního testu:
   ```bash
   pytest -k "nazev_testu"
   ```
Zobrazení podrobného výstupu:
- pytest -v
