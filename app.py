import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.db import get_connection
import pandas as pd

conn = get_connection()

logon_df = pd.read_sql("SELECT * FROM logon", conn)
device_df = pd.read_sql("SELECT * FROM device", conn)
http_df = pd.read_sql("SELECT * FROM http", conn)

active_users = logon_df["user"].nunique()
high_risk_users = (
    device_df.groupby("user")["pc"]
    .nunique()
    .gt(1)
    .sum()
)
http_requests = len(http_df)
active_devices = device_df["pc"].nunique()

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="SentinelX",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# PREMIUM CSS
# ----------------------------

st.markdown("""
<style>

.stApp{
    background:#F8FAFC;
}

/* Remove Streamlit top padding */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:1px solid #E5E7EB;
}

/* Cards */

[data-testid="stMetric"],
[data-testid="stVerticalBlockBorderWrapper"]{

    background:rgba(255,255,255,0.70);

    backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,0.35);

    border-radius:20px;

    padding:20px;

    box-shadow:
    0px 8px 30px rgba(15,23,42,.06);

}

/* Tables */

thead tr th{

    background:#F8FAFC !important;

    color:#334155 !important;

}

tbody{

    font-size:15px;

}

/* Buttons */

.stButton>button{

    border-radius:14px;

    border:1px solid #E2E8F0;

    background:white;

    font-weight:600;

    height:48px;

}

/* Divider */

hr{

    margin-top:25px;

    margin-bottom:25px;

}

</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("SentinelX")

st.sidebar.markdown("---")

st.sidebar.page_link("app.py", label="Dashboard", icon="🏠")

st.sidebar.markdown("### Monitoring")

st.sidebar.write("• Threat Analytics")
st.sidebar.write("• Employee Activity")
st.sidebar.write("• AI Insights")
st.sidebar.write("• Security Logs")

st.sidebar.markdown("---")

st.sidebar.caption("Enterprise v1.0")


# ==========================
# HEADER
# ==========================

left, right = st.columns([6,1])

with left:

    st.markdown("""
    <div style="margin-bottom:20px;">

    <div style="
        font-size:58px;
        font-weight:800;
        color:#0F172A;
        ">
        SentinelX
    </div>

    <div style="
        font-size:20px;
        color:#64748B;
        margin-top:-8px;
        ">
        AI-Powered Insider Threat Detection Platform
    </div>

    </div>
    """, unsafe_allow_html=True)

with right:

    st.button(
        "Administrator",
        use_container_width=True
    )

st.divider()


# ==========================
# KPI CARDS
# ==========================

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.metric(  
            label="Active Users",
            value=active_users,
            delta="+12 Today"
        )

with c2:
    with st.container(border=True):
        st.metric(
            label="High Risk Users",
            value=high_risk_users,
            delta="-1 Today"
        )

with c3:
    with st.container(border=True):
        st.metric(
            label="Alerts Today",
            value=54,
            delta="+6 Today"
        )

with c4:
    with st.container(border=True):
        st.metric(
            label="AI Accuracy",
            value="91%",
            delta="+4%"
        )

st.write("")

st.markdown("---")

st.subheader("AI Insights")

with st.container(border=True):

    st.success("User DTAA/RES0962 logged in from multiple devices within a short period.")

    st.warning("USB device activity increased by 34% compared to yesterday.")

    st.error("Suspicious login detected outside working hours (02:17 AM).")

    st.info("AI Confidence Score: 96.8%")
    
# ============================================================
# THREAT ANALYTICS
# ============================================================

left, right = st.columns([2,1])

# ------------------------------------------------------------
# THREAT ACTIVITY TIMELINE
# ------------------------------------------------------------

with left:

    with st.container(border=True):

        st.subheader("Threat Activity Timeline")

        trend = pd.DataFrame({

            "Day":[
                "Mon",
                "Tue",
                "Wed",
                "Thu",
                "Fri",
                "Sat",
                "Sun"
            ],

            "Threats":[
                4,
                6,
                3,
                8,
                5,
                2,
                4
            ]

        })

        fig = px.line(

            trend,

            x="Day",

            y="Threats",

            markers=True

        )

        fig.update_traces(

            line=dict(
                color="#60A5FA",
                width=4
            ),

            marker=dict(
                size=9,
                color="#3B82F6"
            )

        )

        fig.update_layout(

            height=380,

            template="simple_white",

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            margin=dict(
                l=10,
                r=10,
                t=10,
                b=10
            ),

            xaxis_title="",

            yaxis_title="",

            showlegend=False

        )

        fig.update_xaxes(
            showgrid=False
        )

        fig.update_yaxes(
            gridcolor="#E5E7EB"
        )

        st.plotly_chart(

            fig,

            use_container_width=True,

            config={
                "displayModeBar":False
            }

        )

# ------------------------------------------------------------
# RISK SEVERITY DISTRIBUTION
# ------------------------------------------------------------

with right:

    with st.container(border=True):

        st.subheader("Risk Severity Distribution")

        pie = go.Figure(

            data=[

                go.Pie(

                    labels=[
                        "Low",
                        "Medium",
                        "High"
                    ],

                    values=[
                        117,
                        8,
                        3
                    ],

                    hole=.80,

                    marker=dict(

                        colors=[

                            "#BFDBFE",
                            "#FDE68A",
                            "#FECACA"

                        ]

                    )

                )

            ]

        )

        pie.update_layout(

            height=380,

            margin=dict(
                l=10,
                r=10,
                t=10,
                b=10
            ),

            paper_bgcolor="rgba(0,0,0,0)",

            font=dict(
                size=14
            ),

            showlegend=True

        )

        st.plotly_chart(

            pie,

            use_container_width=True,

            config={
                "displayModeBar":False
            }

        )

st.write("")
st.write("")

st.markdown("---")
st.subheader("Recent Threats")

import pandas as pd

threat_df = pd.DataFrame({
    "Time": [
        "09:14",
        "10:42",
        "11:18",
        "12:05",
        "01:37"
    ],
    "User": [
        "DTAA/RES0962",
        "DTAA/KHO388",
        "DTAA/BJM0992",
        "DTAA/RES0962",
        "DTAA/AMZ0196"
    ],
    "Threat": [
        "USB Device Connected",
        "Multiple Login Attempts",
        "Suspicious HTTP Requests",
        "Unusual Working Hours",
        "Large File Download"
    ],
    "Severity": [
        "🟡 Medium",
        "🔴 High",
        "🟠 Critical",
        "🟡 Medium",
        "🔴 High"
    ]
})

st.dataframe(
    threat_df,
    use_container_width=True,
    hide_index=True
)

# ============================================================
# ENTERPRISE AI RISK SCORE
# ============================================================

st.markdown("## Enterprise AI Risk Score")

gauge = go.Figure(go.Indicator(

    mode="gauge+number",

    value=82,

    number={
        "suffix":"%"
    },

    title={
        "text":"Overall Enterprise Risk"
    },

    gauge={

        "axis":{
            "range":[0,100]
        },

        "bar":{
            "color":"#3B82F6",
            "thickness":0.22
        },

        "steps":[

            {
                "range":[0,40],
                "color":"#ECFDF5"
            },

            {
                "range":[40,70],
                "color":"#FEF3C7"
            },

            {
                "range":[70,100],
                "color":"#FEE2E2"
            }

        ]

    }

))

gauge.update_layout(

    height=300,

    paper_bgcolor="rgba(0,0,0,0)",

    margin=dict(
        l=10,
        r=10,
        t=50,
        b=10
    )

)

st.plotly_chart(

    gauge,

    use_container_width=True,

    config={
        "displayModeBar":False
    }

)

st.write("")


# ============================================================
# EMPLOYEE ANALYTICS + AI INSIGHTS
# ============================================================

left, right = st.columns([2,1])

# ------------------------------------------------------------
# EMPLOYEE TABLE
# ------------------------------------------------------------

with left:

    with st.container(border=True):

        st.subheader("Employee Behaviour Analytics")

        employee = pd.DataFrame({

            "Employee":[
                "Alice",
                "Bob",
                "Charlie",
                "David",
                "Emma",
                "James",
                "Sophia",
                "Michael"
            ],

            "Department":[
                "Finance",
                "IT",
                "HR",
                "Admin",
                "Security",
                "Finance",
                "IT",
                "Admin"
            ],

            "Risk":[
                "High",
                "Medium",
                "Low",
                "High",
                "Low",
                "Medium",
                "Low",
                "High"
            ],

            "Last Activity":[
                "USB Connected",
                "Privilege Escalation",
                "Normal Login",
                "Sensitive File Download",
                "Normal Login",
                "Failed Login",
                "Password Reset",
                "Admin Access"
            ]

        })

        st.dataframe(

            employee,

            use_container_width=True,

            hide_index=True,

            height=330

        )

# ------------------------------------------------------------
# AI INSIGHTS
# ------------------------------------------------------------

with right:

    with st.container(border=True):

        st.subheader("AI Insights")

        st.success("""

**Normal Behaviour**

Most employees are operating within expected behavioural patterns.

""")

        st.warning("""

**Suspicious Behaviour**

Privilege escalation attempt detected for Bob.

""")

        st.error("""

**Critical Threat**

Sensitive document download detected for David.

""")

        st.info("""

**AI Engine**

Isolation Forest

Confidence : 91%

Status : Active

""")

st.write("")
st.write("")



# ============================================================
# SECURITY INCIDENT LOG
# ============================================================

st.markdown("## Security Incident Log")

incident_df = pd.DataFrame({

    "Time":[
        "09:42",
        "10:15",
        "10:56",
        "11:23",
        "12:08",
        "12:46"
    ],

    "Employee":[
        "Alice",
        "Bob",
        "David",
        "James",
        "Michael",
        "Sophia"
    ],

    "Incident":[
        "USB Device Connected",
        "Privilege Escalation Attempt",
        "Sensitive File Download",
        "Multiple Failed Login",
        "Abnormal Login Behaviour",
        "Password Reset"
    ],

    "Severity":[
        "High",
        "Medium",
        "High",
        "Medium",
        "High",
        "Low"
    ],

    "Status":[
        "Investigating",
        "Blocked",
        "Resolved",
        "Investigating",
        "Blocked",
        "Resolved"
    ]

})

st.dataframe(
    incident_df,
    use_container_width=True,
    hide_index=True,
    height=260
)

st.write("")


# ============================================================
# LIVE SECURITY STATUS
# ============================================================

st.markdown("## Live Security Status")

s1, s2, s3 = st.columns(3)

with s1:
    with st.container(border=True):
        st.subheader("Authentication")
        st.success("🟢 Operational")
        st.metric(
            label="Availability",
            value="99.9%"
        )

with s2:
    with st.container(border=True):
        st.subheader("AI Security Engine")
        st.write("Detection Model")
        st.write("Isolation Forest")
        st.success("🟢 Running")

with s3:
    with st.container(border=True):
        st.subheader("Quantum Security")
        st.write("**Algorithm:**")
        st.write("CRYSTALS-Kyber")
        st.success("🟢 Enabled")
        st.write("")


# ============================================================
# PLATFORM INFORMATION
# ============================================================

st.markdown("## Platform Information")

p1, p2, p3 = st.columns(3)

with p1:
    with st.container(border=True):
        st.metric(
            label="Version",
            value="v1.0"
        )

with p2:
    with st.container(border=True):
        st.metric(
            label="Last Scan",
            value="10 seconds ago"
        )

with p3:
    with st.container(border=True):
        st.metric(
            label="Monitoring",
            value="24 × 7"
        )

st.divider()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
"""
<div style="text-align:center;
padding:12px;
font-size:14px;
color:#64748B;">

<b style="font-size:18px;color:#2563EB;">
SentinelX
</b>

<br><br>

AI-Powered Insider Threat Detection &
Privileged Access Monitoring Platform

<br><br>

Finspark Hackathon 2026 Prototype

</div>
""",
unsafe_allow_html=True
)