"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Produce the first data in the recersive list."""
        return self.data
       
    def tail(self) -> Node | None:
        """Produce every node but the 1st one."""
        if (self.next is None):
            return None
        else:
            return self.next 
    
    def last(self) -> int:
        """Returns last data within the nodes."""
        if self.next is None:
            return self.data
        else:
            return self.next.last()