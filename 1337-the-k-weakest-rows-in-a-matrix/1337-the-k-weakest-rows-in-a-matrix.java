class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        int[] rows = new int[k];
        
        ArrayList<Integer> arr = new ArrayList<>();
        ArrayList<Integer> arr1 = new ArrayList<>();
        
        for (int i = 0; i < mat.length; i++) {
            int count = 0;
            for (int j = 0; j < mat[0].length; j++) {
                if (mat[i][j] == 0)
                    break;
                else
                    count++;
            }
            arr.add(count);
            arr1.add(count);
        }
        
        Collections.sort(arr);
        
        for (int l = 0; l < k; l++) {
            rows[l] = arr1.indexOf(arr.get(l));
            arr1.set(arr1.indexOf(arr.get(l)), arr.get(l)-1);
        }
        return rows;
    }
}