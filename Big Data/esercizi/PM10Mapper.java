import java.io.IOException;
import javax.naming.Context;
import org.w3c.dom.Text;

public class PM10Mapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private static final int THRESHOLD = 50;
    private Text sensorId = new Text();
    private final static IntWritable one = new IntWritable(1);

    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] parts = line.split("\t");

        if (parts.length == 3) {
            String sensor = parts[0];
            int pm10Value = Integer.parseInt(parts[2]);

            // Emissione di (sensorId, 1) solo se il valore di PM10 supera la soglia
            if (pm10Value > THRESHOLD) {
                sensorId.set(sensor);
                context.write(sensorId, one);
            }
        }
    }
}
