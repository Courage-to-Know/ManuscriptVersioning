<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" indent="yes" encoding = "utf-8"/>

    <xsl:template match="/">
	<html>
	<head>
	<title>
	     <xsl:for-each select="table">
            <xsl:value-of select="@id"/>
         </xsl:for-each>
	</title>
	<style type="text/css">
		#left{
		<!--line-height:60px;
		background-color:#9acd32;
	    height:500px;-->
		width:;
		float:left;
		padding:0px;
		}
		#content{
		<!-- line-height:40px;
		background-color:;
	    height:100px;-->
		display:flex;
		flex-flow:row wrap;
		width:;
		float:;
		padding-left:0px;
		}
		</style>
	</head>
	<body>
        <h1>
		
          <xsl:for-each select="table">
              <xsl:value-of select="@id"/>
          </xsl:for-each>
        </h1>
    <xsl:for-each select="table">
		<div id="left">
		<table style="border:1px solid" border="1">
                <tr>
				    <th bgcolor="#9ACD32">
                        <xsl:value-of select="rowKeys/@name"/>
				    </th>
				</tr>   				
			<xsl:for-each select="rowKeys/key">
				    <tr>				
						<td bgcolor="#9ACD32">							
							<xsl:value-of select="@value"/>
						</td>
					</tr>
			</xsl:for-each>			
		</table>
		</div>
		<div id="content" contentEditable="True">
		<table style="border:1px solid" border="1">	
		    <tr>
			<xsl:for-each select="fields/field">
				    <th bgcolor="#9ACD32">
					 <span style="padding:left;">
					   <xsl:value-of select="@name"/></span>
					</th> 
		    </xsl:for-each>
			</tr>	   
			<!--/table>
			</div>
			
			<xsl:variable name = "rows">
			<div id="content" contentEditable="true">
			<table border="1"-->
			<xsl:for-each select="data/row">
				    <tr>
						<xsl:call-template name="splitter">
							<xsl:with-param name="remaining-string"  select="@value"/>
							<xsl:with-param name="pattern"  select="'|'"/>
						</xsl:call-template>						
					</tr>
			</xsl:for-each>
            	
		</table>
		</div>
			<!--/xsl:variable>
		<xsl:copy-of select = "$rows"/-->
	</xsl:for-each>
	<ol>	
	    <input type="submit" id="btn_sub" name="btn_sub" value="Submit" />
        <input type="reset" id="btn_res" name="btn_res" value="Reset" /> 
	</ol>
     	</body>
        </html>
</xsl:template>

	<xsl:template name="splitter">
	<xsl:param name="remaining-string"/>
		<xsl:param name="pattern"/>
		<xsl:choose>
			<xsl:when test="contains($remaining-string,$pattern)">
			<td>
			<xsl:value-of select = "normalize-space(substring-before($remaining-string,$pattern))"/>
			<xsl:call-template name="splitter">
					<xsl:with-param name="remaining-string"  select="substring-after($remaining-string,$pattern)"/>
					<xsl:with-param name="pattern"  select="$pattern"/>
			</xsl:call-template>
			</td>
			</xsl:when>
			<xsl:otherwise>
				<td><xsl:value-of select = "normalize-space($remaining-string)"/></td>
			</xsl:otherwise>
		</xsl:choose>	
	</xsl:template>
</xsl:stylesheet>