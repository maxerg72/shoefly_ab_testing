<h1>DESCRIPTION</h1>

This small project analyzes the .csv file of a fictional website called ShoeFly. This website sent 2 kinds of ads through emails, and they also published them
as banner ads on Facebook, X and Google. They provided a file "ad_clicks.csv" which has columns:

  **user_id** => ID of a tracked user
  **utm_source** => Source, on which the user saw the ad (e.g. Facebook, X...)
  **day** => day of the week, on which the user was presented with the ad
  **ad_click_timestamp** => If the user did click on the ad, this column displays the time they spent viewing the ad. If they did not click, the row is empty.
  **experimental_group** => either A or B, shows if the user was shown the ad A or ad B.

This program is meant to analyze this data. When you run the program, two pivot tables are displayed, summarizing my analysis. They show the results of the A/B test, suggesting that
the ad A was more successful, with more clicks on average than the ad B.
