from unittest.mock import patch
from epic_events.controllers.contract_controller import add_contract, \
    get_contracts, get_not_signed_contracts
from epic_events.models import Contract


def test_add_contract(db_session, test_engine):

    new_contract = {
        'amount': '2000',
        'left_to_pay': '500',
    }

    client_id = 1

    with patch('builtins.input', return_value=''):
        add_contract(new_contract, client_id, db_session)

        assert db_session.query(Contract).filter_by(
            amount='2000').first() is not None


def test_get_contracts(db_session, capsys):

    with patch('builtins.input', return_value='0'):
        get_contracts(db_session)
        captured = capsys.readouterr()

        assert "doe" in captured.out


def test_get_not_signed_contracts(db_session, capsys):

    with patch('builtins.input', return_value='0'):
        get_not_signed_contracts(db_session)
        captured = capsys.readouterr()

        assert "doe" in captured.out
