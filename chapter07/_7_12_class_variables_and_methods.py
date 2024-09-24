class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Alternate constructor
    @classmethod
    # The class is passed as argument (cls) solves an important problem related to inheritance.
    def from_xml(cls, data):
        from xml.etree.ElementTree import XML

        doc = XML(data)
        amount_text = doc.findtext("amount") or "0"
        # Same as, Account(..., ...)
        return cls(doc.findtext("owner"), float(amount_text))


data = """
<account>
    <owner>Guido</owner>
    <amount>1000.0</amount>
</account>
"""

a = Account.from_xml(data)
print(vars(a))


# Class method and subclass
class EvilAccount(Account):
    pass


e = EvilAccount.from_xml(data)
print(e)


# Use class variables and class methods to configure and control how instance operate.
import time


class Date:
    datefmt = "{year}-{month:02d}-{day:02d}"

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return self.datefmt.format(year=self.year, month=self.month, day=self.day)

    @classmethod
    def from_timestamp(cls, ts):
        tm = time.localtime(ts)
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

    @classmethod
    def today(cls):
        return cls.from_timestamp(time.time())


# The class variable (datefmt) can be customized via inheritance.
class MDYDate(Date):
    datefmt = "{month}/{day}/{year}"


class DMYDate(Date):
    datefmt = "{day}/{month}/{year}"


a = Date(1967, 4, 9)
print(a)  # 1967-04-09

b = MDYDate(1967, 4, 9)
print(b)  # 4/9/1967

c = DMYDate(1967, 4, 9)
print(c)  # 9/4/1967

a = MDYDate.today()
b = DMYDate.today()
print(a)
print(b)
