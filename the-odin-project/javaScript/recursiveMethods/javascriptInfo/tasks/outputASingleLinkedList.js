function recursivePrintList(head) {
    if (head !== null) {
        console.log(head.value);
        recursivePrintList(head.next);
    }
}

function iterativePrintList(head) {
    // While loop has simpler syntax
    for (let node = head; node !== null; node = node.next) {
        console.log(node.value);
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

