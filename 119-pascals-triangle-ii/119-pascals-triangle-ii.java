class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> pre = null;
        for (int i = 0; i <= rowIndex; i++) {
            List<Integer> cur = new ArrayList<>();
            cur.add(1);
            if ((pre != null) && (i >= 2)) {
                for (int j = 1; j <= i - 1; j++) 
                    cur.add(pre.get(j-1) + pre.get(j)); 
            }
            if (rowIndex > 0)
                cur.add(1);
            if (cur.size() == rowIndex + 1)
                return cur;
            pre = cur;
        }
        return null;
    }
}