class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> aList = new ArrayList<>();
        if (numRows < 1)
            return aList;
        List<Integer> pre = null;
        
        for (int i = 1; i <= numRows; i++) {
            List<Integer> cur = new ArrayList<>();
            cur.add(1);
            if (pre != null && i > 2) {
               for (int j = 1; j <= i - 2; j++) 
                    cur.add(pre.get(j-1) + pre.get(j));
            }
            if (i > 1)
                cur.add(1);
            aList.add(cur);
            pre = cur;
        }
        return aList;
    }
}