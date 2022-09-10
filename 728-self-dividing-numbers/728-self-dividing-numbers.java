class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> aList = new LinkedList<>();
        for (int i = left; i <= right; i++) {
            boolean isValid = true;
            for (char ch : ("" + i).toCharArray()) {
                if (ch - '0' == 0 || (i % (ch - '0') != 0)) {
                    isValid = false;
                    break;
                }
            }
            if (isValid)
                aList.add(i);
        }
        return aList;
    }
}