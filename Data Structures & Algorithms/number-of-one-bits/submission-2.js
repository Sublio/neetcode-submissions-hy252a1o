class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number}
     */
    hammingWeight(n) {
        const binN = n.toString(2);
        let res = 0;
        for (let b of binN){
            const n = parseInt(b, 10);
            if (n == 1){
                res +=1;
            }
        }
        return res;
    }
}
