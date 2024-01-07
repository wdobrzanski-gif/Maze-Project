"""
Module: agenda

Implementations of the Agenda ADT
"""

from abc import ABC, abstractmethod
from typing import Any
from comp120 import Stack, Queue, EmptyStructureError


class AgendaEmpty(Exception):
    """ Raise when try to remove an empty agenda"""
    pass


class Agenda(ABC):
    """Parent/base class for all classes that will implement the Agenda ADT.

    DO NOT MODIFY THIS CLASS IN ANY WAY."""

    @abstractmethod
    def add(self, item: Any) -> None:
        """Adds an item to the agenda."""
        return

    @abstractmethod
    def remove(self) -> Any:
        """Removes and returns an next item on the agenda."""
        return

    @abstractmethod
    def next(self) -> Any:
        """Returns an next item on the agenda."""
        return

    @abstractmethod
    def size(self) -> int:
        """Returns the number of items on the agenda."""
        return 0

    @abstractmethod
    def is_empty(self) -> bool:
        """Returns True if the agenda has no items, and False otherwise."""
        return False



class StackAgenda(Agenda):
    def __init__(self):
        self.agenda = Stack()

    def add(self, item: Any):
        self.agenda.push(item)

    def is_empty(self) -> bool:

        return self.agenda.is_empty()

    def remove(self) -> Any:
        if self.agenda.is_empty():
            raise AgendaEmpty
        return self.agenda.pop()

    def next(self) -> Any:

        if self.agenda.is_empty():
            raise AgendaEmpty

        return self.agenda.peek()

    def size(self) -> int:

        return self.agenda.size()


class QueueAgenda(Agenda):
    def __init__(self):
        self.agenda = Queue()

    def add(self, item: Any):
        self.agenda.enqueue(item)

    def is_empty(self) -> bool:

        return self.agenda.is_empty()

    def remove(self) -> Any:

        if self.agenda.is_empty():
            raise AgendaEmpty
        return self.agenda.dequeue()

    def next(self) -> Any:
        if self.agenda.is_empty():
            raise AgendaEmpty
        return self.agenda.first()

    def size(self) -> int:

        return self.agenda.size()