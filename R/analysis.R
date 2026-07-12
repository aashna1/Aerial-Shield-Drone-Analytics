# -----------------------------
# Aerial Shield Drone Analytics
# R Data Analysis
# -----------------------------

library(ggplot2)
library(dplyr)
library(readr)

setwd("C:/Users/dell/OneDrive/Documents/Aerial-Shield-Drone-Analytics")

df <- read_csv("output/Aerial_Shield_Drone_Data.csv")

print(head(df))
summary(df)

# Create output folder if not present
dir.create("output/R_Graphs", showWarnings = FALSE)

# -----------------------------
# Mission Status
# -----------------------------

p1 <- ggplot(df, aes(Mission_Status, fill = Mission_Status)) +
  geom_bar() +
  ggtitle("Mission Status Distribution") +
  theme_minimal()

ggsave("output/R_Graphs/mission_status.png", p1,
       width = 8, height = 5)

# -----------------------------
# Weather Distribution
# -----------------------------

p2 <- ggplot(df, aes(Weather, fill = Weather)) +
  geom_bar() +
  ggtitle("Weather Distribution") +
  theme_minimal()

ggsave("output/R_Graphs/weather_distribution.png",
       p2,
       width = 8,
       height = 5)

# -----------------------------
# Mission Types
# -----------------------------

p3 <- ggplot(df,
             aes(Mission_Type,
                 fill = Mission_Type)) +
  geom_bar() +
  ggtitle("Mission Types") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 30,
                                   hjust = 1))

ggsave("output/R_Graphs/mission_type.png",
       p3,
       width = 9,
       height = 5)

# -----------------------------
# Battery Consumption
# -----------------------------

p4 <- ggplot(df,
             aes(Battery_Consumed)) +
  geom_histogram(binwidth = 5,
                 fill = "steelblue",
                 color = "white") +
  ggtitle("Battery Consumption")

ggsave("output/R_Graphs/battery_consumption.png",
       p4,
       width = 8,
       height = 5)

# -----------------------------
# Mission Score
# -----------------------------

p5 <- ggplot(df,
             aes(Mission_Score)) +
  geom_histogram(binwidth = 5,
                 fill = "darkgreen",
                 color = "white") +
  ggtitle("Mission Score Distribution")

ggsave("output/R_Graphs/mission_score.png",
       p5,
       width = 8,
       height = 5)

cat("\nAnalysis Complete.\n")