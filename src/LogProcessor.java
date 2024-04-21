import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class LogProcessor {

    public List<String> readLogFile(String filePath) {
        List<String> logEntries = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                logEntries.add(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return logEntries;
    }
}
