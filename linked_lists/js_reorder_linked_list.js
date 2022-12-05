class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function reOrder(head) {
    let array = [head];
    let current = head.next;
    let first, last;

    while (current) {
        array.push(current);
        current = current.next;
    }

    for (let i=0; i<array.length; i++){
        if (!array[i+1]) {
            break;
        }
        
        first = array[i];
        last = array[array.length - 1];

        next = first.next;
        first.next = last;
        last.next = next;
        
        array.pop();
        if (!array[i+2]) next.next = null;
    }

    return head;
}

let listHead1 = new LinkedList(1);
let listHead2 = new LinkedList(2);
let listHead3 = new LinkedList(3);
let listHead4 = new LinkedList(4);
let listHead5 = new LinkedList(5);

listHead1.next = listHead2;
listHead2.next = listHead3;
listHead3.next = listHead4;
listHead4.next = listHead5;

let result = reOrder(listHead1);
console.log(result);