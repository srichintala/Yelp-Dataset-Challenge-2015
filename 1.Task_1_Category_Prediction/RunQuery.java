package YelpCategoryPrediction.QueryConsumerModule;

import java.nio.file.Paths;
import java.util.ArrayList;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.search.similarities.BM25Similarity;
import org.apache.lucene.store.FSDirectory;

import YelpCategoryPrediction.QueryGeneratorModule.FileAccess;

/**
 * @author Renuka
 * Class to kick-start the category prediction module on test index of lucene
 */
public class RunQuery {
	
	public static void main(String[] args) {
		CategoryPredictor sq = new CategoryPredictor();
		
		ArrayList<String> queries = sq.getQueries();
		sq.rankDocsForQuery(queries);
		System.out.println("DONE!!");
	}
	
}
