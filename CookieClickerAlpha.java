package CodeJam;

import java.io.*;
import java.net.URL;
import java.nio.DoubleBuffer;
import java.util.logging.Logger;

/**
 * Created with IntelliJ IDEA.
 * User: aniketzamwar
 * Date: 4/11/14
 * Time: 9:38 PM
 *
 * Google Code Jam 2014
 * https://code.google.com/codejam/contest/2974486/dashboard#s=p1
 */
public class CookieClickerAlpha {
    final static Logger log = Logger.getLogger(CookieClickerAlpha.class.getName());

    public static void timeforcookies(final String file) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(file)))
        {

            String sCurrentLine = br.readLine();
            int count = Integer.parseInt(sCurrentLine);
            int Case = 1;
            while (count > 0) {

                double rate = 2.0F;
                double time = 0.0F;

                sCurrentLine = br.readLine();
                String[] values = sCurrentLine.split(" ");
                double C = Double.parseDouble(values[0]);
                double F = Double.parseDouble(values[1]);
                double X = Double.parseDouble(values[2]);

                double cookies = 0;

                while (cookies < X) {
                    double timeRequiredWithoutByingFarm = (X - cookies)/rate;
                    double secondsToCreateC_Cookies = (C - cookies)/(rate);
                    double secondsBuying;
                    secondsBuying = secondsToCreateC_Cookies + X/(rate + F);
                    if (secondsBuying < timeRequiredWithoutByingFarm) {
                        if(cookies > C) {
                            cookies = cookies - C;
                        }
                        time = time + secondsToCreateC_Cookies;
                        rate = rate + F;
                    } else {
                        cookies = X;
                        time = time + timeRequiredWithoutByingFarm;
                    }
                }
                System.out.format("Case #%d: %.7f%n",Case,time);
                Case = Case + 1;
                count--;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public static void main(String[] args) throws IOException {
        timeforcookies("/Users/aniketzamwar/IdeaProjects/CodeJam2014/src/CodeJam/input1.txt");
    }
}
