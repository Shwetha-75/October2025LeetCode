import org.junit.Assert;
import org.junit.Test;

public class SmallestMissingNonnegativeIntegerAfterOperationsTest {
    @Test
    public void test(){
           SmallestMissingNonnegativeIntegerAfterOperations object=new SmallestMissingNonnegativeIntegerAfterOperations();
           
           int[] nums_1={1,-10,7,13,6,8};

           Assert.assertEquals(4, object.findSmallestInteger(nums_1,7 ));
    }


}
