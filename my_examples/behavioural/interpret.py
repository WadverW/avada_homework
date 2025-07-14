from abc import ABC, abstractmethod
import random
### codes

class Expression(ABC):

    @abstractmethod
    def interpret(self, codes: set, passwords: set) -> bool:
        pass


class Code(Expression):
    def __init__(self, code: int, password: str):
        self.code = int(code)
        self.password = password

    def interpret(self, codes: set, passwords: set) -> bool:
        return self.code in codes and self.password in passwords

class CombABC(Expression, ABC):
    def __init__(self, main_code: Expression, second: Expression = None):
        self.main_code = main_code
        self.second = second


class SuccessCombination(CombABC):
    def __init__(self, main_code, second):
        super().__init__(main_code, second)

    def interpret(self, codes: set, passwords: set) -> bool:
        return self.main_code.interpret(codes, passwords) and self.second.interpret(codes, passwords)


class VerifyCombination(CombABC):
    def __init__(self, main_code, extra):
        super().__init__(main_code)
        self.extra = extra

    def interpret(self, codes: set, passwords: set) -> bool:
        return self.main_code.interpret(codes, passwords) and self.extra.interpret(codes, passwords)

# class Breach(CombABC):



if __name__ == "__main__":
    extra_int = random.randint(10000, 50000)
    extra_str = random.choice(["taro", "omega", "fargo", "veritas"])
    codes = {55777, 33577, extra_int}
    passwords = {"alpha", "beta", extra_str}

    success = SuccessCombination(
        Code(5577, "beta"),
        Code(33577, "omega")
    )

    res_ = success.interpret(codes, passwords)

    if res_:
        print("Access Granted!")
    else:
        verify_case = VerifyCombination(
            Code(55777, "beta"),
            Code(extra_int, extra_str)
        )
        res = verify_case.interpret(codes, passwords)
        if not res:
            print("Access Denied!")
        else:
            print("Access Granted!")
