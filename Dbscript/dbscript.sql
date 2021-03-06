USE [GeoLens]
GO
/****** Object:  Table [dbo].[Profile_Details]    Script Date: 5/30/2021 4:06:57 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Profile_Details](
	[ProfileId] [int] IDENTITY(1,1) NOT NULL,
	[FName] [nvarchar](50) NOT NULL,
	[LName] [nvarchar](50) NOT NULL,
	[mailId] [nvarchar](50) NOT NULL,
	[PhoneNumber] [nvarchar](20) NOT NULL,
	[BloodGroup] [nvarchar](4) NULL,
	[UserName] [nvarchar](50) NOT NULL,
	[CreatedOn] [smalldatetime] NOT NULL,
	[ModifiedOn] [smalldatetime] NOT NULL,
	[IsActive] [bit] NOT NULL,
 CONSTRAINT [PK_Profile_Details] PRIMARY KEY CLUSTERED 
(
	[ProfileId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
