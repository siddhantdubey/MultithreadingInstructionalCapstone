import java.util.List;

public class MetricsCalculator {

    public int calculateTotalRequests(List<String> logEntries) {
        return logEntries.size();
    }
}