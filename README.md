# MetricMind

## 📌 Introduction  
In today’s data-driven world, businesses generate massive volumes of information across regions and operations. To support informed decision-making, this project implements a **real-time executive dashboard** for monitoring key performance indicators (KPIs), including **sales trends, customer engagement, and inventory levels**.  

By leveraging **Big Data technologies** and interactive visualisation tools, the dashboard provides executives with actionable insights, enabling them to adapt strategies across multiple countries with agility and precision.  

---

## 🎯 Objectives  
- Develop an executive dashboard to visualize critical KPIs.  
- Track and analyze **sales**, **customer engagement**, and **inventory health**.  
- Provide executives with **interactive tools** for deep operational insights.  
- Employ scalable **big data processing and visualization** techniques.  

---

## 📂 Dataset  
- A **synthetic dataset** was created to simulate real-world business data across **five countries**: USA, Canada, France, Germany, and Mexico.  
- Reference dataset adapted from Kaggle: [Product Sales Dataset](https://www.kaggle.com/datasets/anuchhetry/product-sales).  
- Key attributes include:  
  - Segment, Country, Product, Discounts  
  - Units Sold, Manufacturing Price, Sales Price  
  - Gross Sales, Profit, COGS, Date  

---

## ⚙️ Technologies Used  
- **Hadoop** – distributed storage of large datasets.  
- **Apache Spark / PySpark** – fast distributed data processing & KPI computation.  
- **Plotly & Dash** – interactive web-based visualization and dashboarding.  
- **Pandas** – structured data manipulation.  
- **Tableau & Power BI** – alternative/complementary visualization tools.  
- **SQL** – querying and filtering structured datasets.  
- **Jupyter Notebook** – exploration and prototype development.  

---

## 🚀 Implementation Steps  
1. **Data Preparation**  
   - Cleaned and normalised the raw dataset.  
   - Derived KPIs: total sales, engagement rates, and stock levels.  

2. **Big Data Processing**  
   - Used **PySpark** for distributed filtering, aggregations, and transformations.  
   - Converted Spark DataFrames to Pandas for visualisation.  

3. **Visualization & Dashboard**  
   - Built interactive charts (line, bar, pie, scatter, gauge) in **Dash + Plotly**.  
   - Dashboard includes navigation by country, time, and KPIs.  

---

## 📊 Results  
- The dashboard enables executives to:  
  - Compare **sales growth** across regions (e.g., USA peaks in February, while Mexico underperforms).  
  - Assess **customer engagement patterns** (France and Canada show higher engagement).  
  - Monitor **inventory efficiency**, identifying supply chain gaps (e.g., consistently low stock in Mexico).  

- **Scalability**: The system can handle millions of rows, with Spark ensuring performance and responsiveness.  
- **Business Value**: Delivers **real-time insights** for strategy optimisation, improved resource allocation, and enhanced decision-making.  

---

## ✅ Conclusion  
This project demonstrates how **Hadoop + Spark** for big data processing, combined with **Dash/Plotly** for interactive visualization, creates a powerful tool for **global business decision-making**. Future enhancements include **real-time data streaming** via Spark Streaming and integration with external sources (e.g., social media sentiment).  
