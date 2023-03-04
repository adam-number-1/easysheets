# Easy sheets project
A python package filled with a lot of convenience functionality, classes and more to make a programatical way of creating and customizing Google sheets much easier.

## How is it built?
The library is a python wrapper around the API, which is referred on the Google sheets API website. The library allows you either using the python counterparts of the Google sheets API methods directly or you can use convenience functionality built on top of this low level API, which reflects the most common workflow, when creating a spreadsheets, by providing a logical layer on top of the low level API.

For example, when you want to create a spreadsheet, you are not thinking about the work in terms of "I want to create a batchUpdate request here and batchUpdate values there..." etc. You are more thinking in term of where to put range of values, where to put a chart, where to create a hyperlink, where to create a colorful background. This library allows you to do exactly that.

With Easysheets package, you will be able to programatically create unlimited amount of Google spreadsheets with less time spent on trying to understand the Google documentation.