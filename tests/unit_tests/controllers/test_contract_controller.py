from unittest.mock import patch, Mock
from epic_events.controllers.contract_controller import add_contract, \
    get_contracts, get_not_signed_contracts

from epic_events.models import Contract


def test_add_contract(db_session, insert_test_client, test_engine):

    insert_test_client(first_name="john", last_name="doe", phone="123456789",
                       company_name="Test company", email="john@example.com",
                       first_contact="2024-08-12 15:30:12", commercial_id=2)

    mock_client = Mock()
    mock_client.commercial_id = 1

    new_contract = {
        'amount': '2000',
        'left_to_pay': '500',
    }

    client_id = 1

    with patch('epic_events.controllers.contract_controller.get_client_datas',
               return_value=mock_client) as mock_func:
        add_contract(new_contract, client_id, db_session)

        mock_func.assert_called_once_with(client_id)
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
