# How to add a new Statute type identity

See the id file: `statute_utils/statute_id.py`.

Each type has an identity represented by a `StatuteID`:

```python
class StatuteID(Enum):
    RA = ("Republic Act", _NUMBER) # `ra` is StatuteID for _Republic Act_
    CA = ("Commonwealth Act", _NUMBER)
    ...
```

Here the names of the `StatuteID` matter since later on, they will be used in the config files, e.g. `ra` will be used in a `yaml` file to indicate that the document is of the type `Republic Act. If we were to create a new type, we'd have to declare the following entry:

```python
class StatuteID(Enum):
    RA = ("Republic Act", _NUMBER)
    CA = ("Commonwealth Act", _NUMBER)
    SC_CIR = ("SC Circular", _NUMBER) # new
```

## How to create a new Statute type formula

See the serials file: `statute_utils/formula/serials.py`.

This contains classes of formula representing specific identities.

Each identity needs a formulae which is the raw regex pattern string.

To create a new one, the class must follow the following format:

```python
class SampleNameOfIdentity(StatutePatternsMethods):
    statute_id = StatuteID.RA.name # this is the reference to the identity above
    group_name = "unique_name_for_capturing_named_group" 
    digit_group_name = "unique_name_for_capturing_named_digits"
    # the reason for requiring uniqueness is that this formula will be concatenated with other formulas so it needs to have a unique identifier; see sample formula below

    def __init__(self) -> None:
        self.formula = rf"""
        ( 
            \b
            (?P<{self.group_name}> 
                (Republic\s+Act)|
                (Rep\.\s+Act)
                (Rep\s+Act)
                RA|
            ) # e.g. Republic Act
            \s+ # need one space
            (No\.\s*)?, # optional No.
            (?P<{self.digit_group_name}>[\w-]+) # 386-A 
        )
        """
```

## Include formula in compiled statute regexes

1. See the formula __init__ file: `statute_utils/formula/__init__.py` in relation to the `statute_utils/compiler.py`
2. Add latest formula you created from `serials` to this `__init__`.
3. Include the added formula in the `compiler` file

```python
statutory_regexes = [
    NamedStatute.formula,  # special patterns
    RepublicAct().formula,
    CommonwealthAct().formula,
    YOURNEWCLASSCREATED().formula # your new identitied formula
    NamedStatuteIndeterminate.formula, # special patterns
```

## How to test the identity-formula

See the serials file: `tests/test_statute_formula.py` file. The `STATUTE_FORMULA_TEST_VALUES` variable refers to a list of values. Each value is a tuple or a test of identity, e.g.:

```python
(
    "RULE_RESO",
    "Resolution of the Court En Banc dated",
    "1-1-1990",
    "Resolution of the Court En Banc dated 1-1-1990",
),
```

This means that:

`StatuteID` with name `RULE_RESO` should match the following pattern: "Resolution of the Court En Banc dated 1-1-1990", resulting in two parts: the original pattern `Resolution of the Court En Banc` and the joined value `1-1-1990`.
