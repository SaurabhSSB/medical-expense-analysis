library(tidyverse)
m_expenses <- read.csv("C:/Users/Hp/Desktop/medical_expenses.csv")

head(m_expenses)

str(m_expenses)

summary(m_expenses)

colSums(is.na(m_expenses))

# Visualize relationships
ggplot(m_expenses, aes(x = age, y = charges)) + geom_point() + geom_smooth() + ggtitle("Charges vs Age")
ggplot(m_expenses, aes(x = bmi, y = charges)) + geom_point() + geom_smooth() + ggtitle("Charges vs BMI")
ggplot(m_expenses, aes(x = children, y = charges)) + geom_point() + geom_smooth() + ggtitle("Charges vs No. of Children")
ggplot(m_expenses, aes(x = as.factor(children), y = charges)) + geom_boxplot() + ggtitle("Charges vs Smoker")

# Categorical vs Numerical
ggplot(m_expenses, aes(x = smoker, y = charges)) + geom_boxplot() + ggtitle("Charges vs Smoker")
ggplot(m_expenses, aes(x = region, y = charges)) + geom_boxplot() + ggtitle("Charges vs Region")
ggplot(m_expenses, aes(x = gender, y = charges)) + geom_boxplot() + ggtitle("Charges vs Gender")

# Boxplot of charges by smoker status
ggplot(m_expenses, aes(x = smoker , y = charges)) + 
  geom_boxplot(fill = c("lightblue", "lightcoral")) + 
  labs(title = "Charges by Smoker Status")

# Boxplot of charges by non-smoker status with gender 
# Create the boxplot
ggplot(m_expenses, aes(x = gender, y = charges, fill = smoker)) +
  geom_boxplot() +
  labs(
    title = "Medical Charges by Smoker Status and Gender",
    x = "Gender",
    y = "Medical Charges"
  )

# Boxplot of charges by non-smoker status with region 
# Create the boxplot
ggplot(m_expenses, aes(x = region, y = charges, fill = smoker)) +
  geom_boxplot() +
  labs(
    title = "Medical Charges by Smoker Status and Region",
    x = "Region",
    y = "Medical Charges"
  )

# Create the scatter plot with color-coded points based on smoker status
ggplot(m_expenses, aes(x = bmi, y = charges, color = smoker)) +
  geom_point() +
  labs(
    title = "Medical Charges vs. BMI by Smoker Status",
    x = "BMI",
    y = "Medical Charges"
  )

# Create the scatter plot with color-coded points based on smoker status
ggplot(m_expenses, aes(x = age, y = charges, color = smoker)) +
  geom_point() +
  labs(
    title = "Medical Charges vs. Age by Smoker Status",
    x = "Age",
    y = "Medical Charges"
  )

# Create the scatter plot with color-coded points based on smoker status
ggplot(m_expenses, aes(x = as.factor(children), y = charges, fill = smoker)) +
  geom_boxplot() +
  labs(
    title = "Medical Charges by Smoker Status and No. of Children",
    x = "No. of Children",
    y = "Medical Charges"
  )
ggplot(m_expenses, aes(x = children, y = charges, color = smoker)) +
  geom_point() +
  labs(
    title = "Medical Charges vs. No. of Children by Smoker Status",
    x = "No. of Children",
    y = "Medical Charges"
  )

m_expenses_grouped <- group_by(m_expenses, smoker)
summarise(m_expenses_grouped, 
          mean_charge = mean(charges))

smoker_counts <- table(m_expenses$smoker)
print(smoker_counts)
