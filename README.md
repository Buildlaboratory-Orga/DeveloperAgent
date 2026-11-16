# DeveloperAgent
This Repo is for the modul "Artificial Intelligence and Virtual Robotics"

## Inhalt

`mathtools/` enthält 13 kleine Module mit einfachen mathematischen Funktionen.
Sie dienen als Testobjekt für den Agent-Workflow: Jira-Bug-Ticket → Agent analysiert den Code → Fix.

| Modul | Funktionen |
|---|---|
| `basic_ops.py` | `add`, `subtract`, `multiply`, `divide` |
| `powers.py` | `square`, `cube`, `power`, `square_root` |
| `stats.py` | `mean`, `median`, `minimum`, `maximum`, `value_range` |
| `geometry.py` | `rectangle_area`, `rectangle_perimeter`, `triangle_area`, `circle_area`, `circle_circumference` |
| `percentages.py` | `percent_of`, `percent_change`, `apply_discount`, `add_vat` |
| `number_theory.py` | `is_even`, `is_prime`, `gcd`, `lcm` |
| `sequences.py` | `factorial`, `fibonacci`, `sum_up_to` |
| `conversions.py` | `celsius_to_fahrenheit`, `fahrenheit_to_celsius`, `km_to_miles`, `miles_to_km` |
| `finance.py` | `simple_interest`, `compound_interest`, `annuity_payment`, `break_even_units` |
| `vectors.py` | `add_vectors`, `scale_vector`, `dot_product`, `vector_length` |
| `matrix.py` | `transpose`, `multiply`, `determinant`, `solve` |
| `regression.py` | `normal_matrix`, `polynomial_fit`, `predict`, `r_squared` |
| `trend.py` | `is_stable`, `trend_report` |

Zu jedem Modul gibt es eine Testdatei in `tests/`.

## Tests ausführen

Benötigt nur Python 3.10+ (keine zusätzlichen Pakete). Im Hauptordner des Repos:

```bash
python3 -m unittest discover -s tests -v
```

Alle Tests sollten grün sein. Schlägt ein Test fehl, ist ein Bug im Code.
