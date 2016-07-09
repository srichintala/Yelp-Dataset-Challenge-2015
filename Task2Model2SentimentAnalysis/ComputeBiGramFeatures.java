/* This program is used to compute bigram features for sentiment analysis
 * Bag of words assumption is used to compute frequencies of each bigram
 * feature generated. Lucene is used to remove stop words, tokenization and
 * generation of bigram features from review text
 * Author : Nayana Charwad
 * */

package preprocessReviews;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.StringReader;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.core.StopAnalyzer;
import org.apache.lucene.analysis.en.PorterStemFilter;
import org.apache.lucene.analysis.shingle.ShingleFilter;
import org.apache.lucene.analysis.tokenattributes.CharTermAttribute;

public class ComputeBiGramFeatures {

	public static void main(String[] args) throws IOException {
		
		String filePath = "RatingFinal.csv";
		FileReader input = new FileReader(filePath);
		BufferedReader inputReader = new BufferedReader(input);		
		String line = null;
		HashMap<String,Integer> countMap = new HashMap<String,Integer>();
		int lineCount = 0;
		
		while((line = inputReader.readLine())!=null)
		{
			//stop analyzer to remove stop words
			Analyzer analyzer = new StopAnalyzer();
			TokenStream tokenStream = analyzer.tokenStream("contents", new StringReader(line));
			tokenStream = new PorterStemFilter(tokenStream);
			
			//ShingleFiler is used to generate bigrams
			ShingleFilter sf = new ShingleFilter(tokenStream,2,2);
			sf.setOutputUnigrams(false);
			
			CharTermAttribute charTermAttribute = sf.addAttribute(CharTermAttribute.class);
		    sf.reset();
		    
		    //generate bigram tokens
		    while (sf.incrementToken()) {
		        String term = charTermAttribute.toString();
		        
		        if(!term.contains("_"))
		        {
		        	//count token frequency
			        if(countMap.containsKey(term))
			        {
			        	int oldCount = countMap.get(term);
			        	countMap.put(term, oldCount+1);
			        }
			        else
			        {
			        	countMap.put(term, 1);
			        }
			    }
		    }
		    analyzer.close();
		    sf.close();
		    lineCount++;
		    if((lineCount % 5000)==0)
		    {
		    	System.out.println("Processed Lines : " + lineCount);
		    }
		}
		
		inputReader.close();

		//write bigram features with generated frequencies in outout file
		FileWriter output = new FileWriter("/Users/Nayana/Desktop/BiGramFeatures5.csv");
		BufferedWriter outputWriter = new BufferedWriter(output);	
		
		Iterator it = countMap.entrySet().iterator();
	    while (it.hasNext()) {
	        Map.Entry pair = (Map.Entry)it.next();
	        outputWriter.write("\n" + pair.getKey() + "," + pair.getValue());
	    }
	    
	    outputWriter.close();
	}
}
