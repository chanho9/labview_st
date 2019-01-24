<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="18008000">
	<Item Name="내 컴퓨터" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">내 컴퓨터/VI 서버</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">내 컴퓨터/VI 서버</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="LabviewTest.vi" Type="VI" URL="../LabviewTest.vi"/>
		<Item Name="PythonConfigGlobal.vi" Type="VI" URL="../PythonConfigGlobal.vi"/>
		<Item Name="sta_Covarance Matrix(SubVI).vi" Type="VI" URL="../sta_Covarance Matrix(SubVI).vi"/>
		<Item Name="sta_error calculator (SubVI).vi" Type="VI" URL="../sta_error calculator (SubVI).vi"/>
		<Item Name="sta_initialize(SubVI).vi" Type="VI" URL="../sta_initialize(SubVI).vi"/>
		<Item Name="sta_make linear equation (SubVI).vi" Type="VI" URL="../sta_make linear equation (SubVI).vi"/>
		<Item Name="sta_makeFactorsMatrix(SubVI).vi" Type="VI" URL="../sta_makeFactorsMatrix(SubVI).vi"/>
		<Item Name="sta_std and variance (SubVI).vi" Type="VI" URL="../sta_std and variance (SubVI).vi"/>
		<Item Name="surface analysis.vi" Type="VI" URL="../surface analysis.vi"/>
		<Item Name="의존성" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="NI_AALBase.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALBase.lvlib"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="NI_Gmath.lvlib" Type="Library" URL="/&lt;vilib&gt;/gmath/NI_Gmath.lvlib"/>
			</Item>
			<Item Name="lvanlys.dll" Type="Document" URL="/&lt;resource&gt;/lvanlys.dll"/>
			<Item Name="PythonVersionsEnum.ctl" Type="VI" URL="../../../../../Program Files (x86)/National Instruments/LabVIEW 2018/examples/Connectivity/Python/support/PythonVersionsEnum.ctl"/>
		</Item>
		<Item Name="빌드 스펙" Type="Build"/>
	</Item>
</Project>
