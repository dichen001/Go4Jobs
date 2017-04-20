Reservoir Sampling

Problem:
	Select K items from N and make sure the items are selected with P=K/N. (N could be very large and unknown)

Solution:
	First put K items in the box/reservoir, then for the rest items, each of them has P=K/(K+i) to be selected and P=1/K to replace one currently in the box/reservoir.

### Problem:
  - Choose <code>k</code> entries from <code>n</code> numbers. Make sure each number is selected with the probability of <code>k/n</code>

### Basic idea:
  - Choose <code>1, 2, 3, ..., k</code> first and put them into the reservoir.
  - For <code>k+1</code>, pick it with a probability of <code>k/(k+1)</code>, and randomly replace a number in the reservoir.
  - For <code>k+i</code>, pick it with a probability of <code>k/(k+i)</code>, and randomly replace a number in the reservoir.
  - Repeat until <code>k+i</code> reaches <code>n</code>

### Proof:
  - For <code>k+i</code>, the probability that it is selected and will replace a number in the reservoir is <code>k/(k+i)</code>
  - For a number in the reservoir before (let's say <code>X</code>), the probability that it keeps staying in the reservoir is
    - <code>P(X was in the reservoir last time)</code> × <code>P(X is not replaced by k+i)</code>
    - = <code>P(X was in the reservoir last time)</code> × (<code>1</code> - <code>P(k+i is selected and replaces X)</code>)
    - = <code>k/(k+i-1)</code> × （<code>1</code> - <code>k/(k+i)</code> × <code>1/k</code>）
    - = <code>k/(k+i)</code>
  - When <code>k+i</code> reaches <code>n</code>, the probability of each number staying in the reservoir is <code>k/n</code>

### Example
  - Choose <code>3</code> numbers from <code>[111, 222, 333, 444]</code>. Make sure each number is selected with a probability of <code>3/4</code>
  - First, choose <code>[111, 222, 333]</code> as the initial reservior
  - Then choose <code>444</code> with a probability of <code>3/4</code>
  - For <code>111</code>, it stays with a probability of
    - <code>P(444 is not selected)</code> + <code>P(444 is selected but it replaces 222 or 333)</code>
    - = <code>1/4</code> + <code>3/4</code>*<code>2/3</code>
    - = <code>3/4</code>
  - The same case with <code>222</code> and <code>333</code>
  - Now all the numbers have the probability of <code>3/4</code> to be picked

### This Problem <Linked List Random Node>
  - This problem is the sp case where <code>k=1</code>



