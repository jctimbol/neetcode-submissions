class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
        int leftIndex = 0;
        int rightIndex = numbers.length - 1;
        int[] indices = new int[2];

        for(int i = 0; i < numbers.length; i++)
        {
            int sum = numbers[leftIndex] + numbers[rightIndex];

            if(sum == target)
            {
                indices[0] = leftIndex + 1;
                indices[1] = rightIndex + 1;
            }
            else if(sum < target)
            {
                leftIndex++;
            }
            else
            {
                rightIndex--;
            }
        }

        return indices;
    }
}
