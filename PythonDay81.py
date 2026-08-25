# Hybrid Inheritance Example:
class BaseClass:
    pass

class DerivedOne(BaseClass):
    pass

class DerivedTwo(BaseClass):
    pass

class DerivedThree(DerivedOne, DerivedTwo):
    pass

# Hierarchical Inheritance Example
class BaseClass2:
    pass

class DerivedFour(BaseClass):
    pass

class DerivedFive(BaseClass):
    pass

class DerivedSix(DerivedFour):
    pass

class DerivedSeven(DerivedFive):
    pass

