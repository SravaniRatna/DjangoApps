from django.shortcuts import render

from django.http import HttpResponse
def emp(request):
 str1="""
    <html>
    <body bgcolor="yellow">
    <table border=5>
    <caption>EMP Details</caption>
    <tr>
    <th>EmpId</th>
    <th>EmpName</th>
    <th>Salary</th>
    </tr>
    <tr>
    <td>101</td>
    <td>Suresh</td>
    <td>40000</td>
    </tr>
    <tr>
    <td> 102 </td>
    <td> Ramesh </td>
    <td> 50000 </td>
    </tr>
    </table>
    </body>
    </html>
    """
 return HttpResponse(str1)

def cust(request):
 str2="""
 <html>
    <body bgcolor="pink">
    <table border=5>
    <caption>CUSTOMER Details</caption>
    <tr>
    <th>CId</th>
    <th>CName</th>
    <th>Salary</th>
    </tr>
    <tr>
    <td>401</td>
    <td>Manoj</td>
    <td>45000</td>
    </tr>
    <tr>
    <td> 402 </td>
    <td> Deva</td>
    <td> 60000 </td>
    </tr>
    </table>
    </body>
    </html>
    """
 return HttpResponse(str2)

