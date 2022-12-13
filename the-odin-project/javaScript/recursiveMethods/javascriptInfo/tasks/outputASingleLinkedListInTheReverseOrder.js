function iterativePrintListInReverse(head) {
    const valuesInOrder = [];
    let node = head;
    while (node) {
        valuesInOrder.push(node.value);
        node = node.next;
    }
    for (let i = valuesInOrder.length - 1; i >= 0; i -= 1) {
        console.log(valuesInOrder[i]);
    }
}

function recursivePrintListInReverse(head) {
    if (head !== null) {
        recursivePrintListInReverse(head.next);
        console.log(head.value);
    }
}

let list = {
  value: 1,
  next: {
    value: 2,
    next: {
      value: 3,
      next: {
        value: 4,
        next: null
      }
    }
  }
};
