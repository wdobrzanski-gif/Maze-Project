"""
Module: test_agenda

pytest module for the StackAgenda and QueueAgenda classes.
"""
import pytest
from agenda import StackAgenda, QueueAgenda


def test_stack_is_empty():
    """ Tests that the StackAgenda's is_empty method works for both empty and
    non-empty agendas. """
    agenda = StackAgenda()

    assert agenda.is_empty() == True # checks that it starts out as empty

    # TODO: add an item to the agenda and check that is_empty returns false
    
    assert agenda.is_empty() == True


# TODO: Write the rest of your pytest test case functions for your StackAgenda and
# QueueAgenda classes below this line. You should have a total of 11 different
# test cases/functions (in addition to the one already defined above).


# DO NOT change anything below this line
if __name__ == "__main__":
    pytest.main(['test_agenda.py'])
