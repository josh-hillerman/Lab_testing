import pytest
from bank import Account

def test_initial_balance():
    account = Account("Daniel", 120)
    assert account.get_balance

def test_deposit():
    account = Account("Daniel", 120)
    account.deposit(50)
    assert account.get_balance == 170
def test_withdraw():
    account = Account("Daniel", 120)
    account.withdraw(30)
    assert account.get_balance == 140
       
def test_deposit_negative_amount():
    account = Account("Daniel", 150)
    with pytest.raises(ValueError, match ="poor"):
        account.withdraw(1250)

def test_withdraw_more_than_balance(): 
    account = Account("Daniel", 150)
    with pytest.raises(ValueError, match ="not enough money"):
        account.withdraw(1620)

def test_withdraw_negative_amount():
    account = Account("Daniel", 150)
    with pytest.raises(ValueError, match ="not enough money"):
        account.withdraw(1050)