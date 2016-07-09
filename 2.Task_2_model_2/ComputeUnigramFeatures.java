/* This program is used to compute unigram features for sentiment analysis
 * Bag of words assumption is used to compute frequencies of each unigram
 * feature generated. Lucene is used to remove stop words, tokenization and
 * generation of unigram features from review text
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
import org.apache.lucene.analysis.tokenattributes.CharTermAttribute;

public class ComputeUnigramFeatures {

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
			
			//tokenstream class to generate unigram tokens
			TokenStream tokenStream = analyzer.tokenStream("contents", new StringReader(line));
			tokenStream = new PorterStemFilter(tokenStream);
			CharTermAttribute charTermAttribute = tokenStream.addAttribute(CharTermAttribute.class);
		    tokenStream.reset();
		    
		    //get individual tokens
		    while (tokenStream.incrementToken()) {
		        String term = charTermAttribute.toString();
		        //count frequencies
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
		    analyzer.close();
		    tokenStream.close();
		    lineCount++;
		    if((lineCount % 5000)==0)
		    {
		    	System.out.println("Processed Lines : " + lineCount);
		    }
		}
		
		inputReader.close();

		//write unigram feature and frequency to generated feature file
		FileWriter output = new FileWriter("/Users/Nayana/Desktop/Features4.csv");
		BufferedWriter outputWriter = new BufferedWriter(output);	
		
		Iterator it = countMap.entrySet().iterator();
	    while (it.hasNext()) {
	        Map.Entry pair = (Map.Entry)it.next();
	        outputWriter.write("\n" + pair.getKey() + "," + pair.getValue());
	    }
	    
	    outputWriter.close();
	}
}
