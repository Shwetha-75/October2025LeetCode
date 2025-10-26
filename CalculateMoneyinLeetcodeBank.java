class CalculateMoneyinLeetcodeBank{
    class Solution{

    public int totalMoney(int n) {
        int total=0,money=1,dollar=1,count=1;
        while(n!=0){
           if(count>7){
              count=1;
              dollar++;
              money=dollar;
           }

           total+=money; 
           money++;
           count++;
           n--;

        } 


        return total;
        
    }

    }
}