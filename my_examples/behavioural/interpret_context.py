from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: set) -> bool:
        pass


class RoleExpression(Expression):
    def __init__(self, role: str):
        self.role = role

    def interpret(self, context: set) -> bool:
        return self.role in context


class AndExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context: set) -> bool:
        return self.left.interpret(context) and self.right.interpret(context)


class OrExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context: set) -> bool:
        return self.left.interpret(context) or self.right.interpret(context)


class NotExpression(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr

    def interpret(self, context: set) -> bool:
        return not self.expr.interpret(context)


if __name__ == "__main__":
    user_roles = {"user", "admin"}

    expr1 = AndExpression(RoleExpression("user"), RoleExpression("admin"))
    expr2 = OrExpression(RoleExpression("user"), RoleExpression("banned"))
    expr3 = NotExpression(RoleExpression("banned"))

    print(f"user AND admin: {expr1.interpret(user_roles)}")
    print(f"user OR banned: {expr2.interpret(user_roles)}")
    print(f"NOT banned: {expr3.interpret(user_roles)}")
