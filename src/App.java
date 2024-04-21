import java.util.List;

public class App {
    public static void main(String[] args) throws Exception{
        String logFilePath = "src/data/web_server_logs.txt";
        
        LogProcessor logProcessor = new LogProcessor();
        System.out.println("Reading log file...");
        List<String> logEntries = logProcessor.readLogFile(logFilePath);
        
        // Calculate metrics
        MetricsCalculator metricsCalculator = new MetricsCalculator();
        int totalRequests = metricsCalculator.calculateTotalRequests(logEntries);
        System.out.println("Total Requests: " + totalRequests);
        
        // Detect anomalies
        AnomalyDetector anomalyDetector = new AnomalyDetector();
        anomalyDetector.detectAnomalies(logEntries);
    }
}
