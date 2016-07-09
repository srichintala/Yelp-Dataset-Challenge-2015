package YelpCategoryPrediction.QueryGeneratorModule;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.Set;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;


/**
 * @author Renuka
 * Class to kick-start the query generation module
 */
public class QueryGenerator {

	public static ArrayList<String> categories;
	public static ArrayList<String> queryTermsLst = new ArrayList<String>();
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		QueryGenerator qg = new QueryGenerator();
		qg.setQuery();
		qg.buildQueriesForCategories();
	
	}
	
	/**
	 * Function to read all queries from categories.txt file into an array
	 */
	public void setQuery(){
		FileAccess fa = new FileAccess();
		categories = fa.ReadFromFile(fa.getIndexFile());;
	}
	
	
	/**
	 * Function to kick-start the query building module from categories
	 */
	public void buildQueriesForCategories(){
		QueryOptimizer qz = new QueryOptimizer();
		//initialize lucene reader and searcher 
		qz.initIndex();
		
		//kick-start the query building module
		qz.buildQueries(categories);
	}
	
}
