from unittest.mock import patch

from epic_events.views.contract_view import display_ask_contract_to_edit


def test_display_ask_contract_to_edit(db_session, capsys):

    with patch('builtins.input', side_effect=['1', 'y']):

        contract_to_edit = display_ask_contract_to_edit(db_session)

        assert contract_to_edit.commercial_id == 1
