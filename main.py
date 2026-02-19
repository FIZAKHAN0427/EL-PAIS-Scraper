import json
import os
from src.scraper import setup_driver, scrape_articles
from src.translator import translate_to_english
from src.analyzer import find_repeated_words


def main():

    driver = setup_driver()
    articles = scrape_articles(driver)
    driver.quit()

    print("\n" + "="*50)
    print("TRANSLATING TITLES")
    print("="*50)

    translated_titles = []
    results = []

    for i, article in enumerate(articles, 1):
        
        spanish_title = article["title"]
        english_title = translate_to_english(spanish_title)
        translated_titles.append(english_title)

        print(f"\n{'='*16} ARTICLE {i} {'='*16}")
        print(f"\nSpanish Title:\n{spanish_title}")
        print(f"\nEnglish Title:\n{english_title}")
        print(f"\nSpanish Content:\n{article['content']}")
        print(f"\nImage:\nimages/article_{i}.jpg")
        print("="*50)

        results.append({
            "article_number": i,
            "spanish_title": spanish_title,
            "spanish_content": article["content"],
            "english_title": english_title,
            "image_path": article["image_path"]
        })

    repeated = find_repeated_words(translated_titles, min_count=2)

    print("\n" + "="*50)
    print("REPEATED WORDS (>2 times)")
    print("="*50)

    if repeated:
        for word, count in sorted(repeated.items(), key=lambda x: x[1], reverse=True):
            print(f"{word}: {count}")
    else:
        print("No repeated words found")

    print("="*50)

    os.makedirs("output", exist_ok=True)
    
    output_data = {
        "articles": results,
        "repeated_words": repeated
    }

    with open("output/results.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print("\n✓ Results saved to output/results.json")


if __name__ == "__main__":
    main()
