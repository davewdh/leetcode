class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> aList = new ArrayList<>();
        for (int i = left; i <= right; i++) {
            boolean isValid = true;
            for (int j = i; j > 0; j /= 10) {
                if (j % 10 == 0 || (i % (j % 10) != 0)) {
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