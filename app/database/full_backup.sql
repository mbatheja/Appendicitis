--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: diagnosis; Type: TABLE; Schema: public; Owner: dadb
--

CREATE TABLE public.diagnosis (
    diagnosis_id integer NOT NULL,
    diagnosis character varying(50) NOT NULL,
    score double precision,
    visit_id integer
);


ALTER TABLE public.diagnosis OWNER TO dadb;

--
-- Name: exam; Type: TABLE; Schema: public; Owner: dadb
--

CREATE TABLE public.exam (
    clinical_id integer NOT NULL,
    peritonitis character varying(20),
    migratory_pain character varying(20),
    lower_right_abd_pain character varying(20),
    contralateral_rebound_tenderness character varying(20),
    ipsilateral_rebound_tenderness character varying(20),
    coughing_pain character varying(20),
    psoas_sign character varying(20),
    nausea character varying(20),
    loss_of_appetite character varying(20),
    body_temperature double precision,
    dysuria character varying(20),
    stool character varying(20),
    visit_id integer
);


ALTER TABLE public.exam OWNER TO dadb;

--
-- Name: lab; Type: TABLE; Schema: public; Owner: dadb
--

CREATE TABLE public.lab (
    lab_id integer NOT NULL,
    neutrophil_percentage double precision,
    wbc_count double precision,
    neutrophilia character varying(20),
    ketones_in_urine character varying(20),
    rdw double precision,
    hemoglobin double precision,
    rbc_count double precision,
    rbc_in_urine character varying(20),
    thrombocyte_count double precision,
    wbc_in_urine character varying(20),
    visit_id integer
);


ALTER TABLE public.lab OWNER TO dadb;

--
-- Name: patient; Type: TABLE; Schema: public; Owner: dadb
--

CREATE TABLE public.patient (
    patient_id integer NOT NULL,
    f_name character varying(50) NOT NULL,
    l_name character varying(50) NOT NULL,
    age double precision,
    gender character varying(10)
);


ALTER TABLE public.patient OWNER TO dadb;

--
-- Name: physician; Type: TABLE; Schema: public; Owner: dadb
--

CREATE TABLE public.physician (
    physician_id integer NOT NULL,
    f_name character varying(50) NOT NULL,
    l_name character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE public.physician OWNER TO dadb;

--
-- Name: visit; Type: TABLE; Schema: public; Owner: dadb
--

CREATE TABLE public.visit (
    visit_id integer NOT NULL,
    patient_id integer,
    physician_id integer
);


ALTER TABLE public.visit OWNER TO dadb;

--
-- Name: vital_sign; Type: TABLE; Schema: public; Owner: dadb
--

CREATE TABLE public.vital_sign (
    demographic_id integer NOT NULL,
    height double precision,
    weight double precision,
    bmi double precision,
    visit_id integer
);


ALTER TABLE public.vital_sign OWNER TO dadb;

--
-- Data for Name: diagnosis; Type: TABLE DATA; Schema: public; Owner: dadb
--

COPY public.diagnosis (diagnosis_id, diagnosis, score, visit_id) FROM stdin;
1	appendicitis	6	1
2	appendicitis	5	2
3	appendicitis	6	3
4	appendicitis	7	4
5	appendicitis	4	5
6	appendicitis	8	6
7	appendicitis	8	7
8	appendicitis	6	8
9	appendicitis	7	9
10	appendicitis	6	10
\.


--
-- Data for Name: exam; Type: TABLE DATA; Schema: public; Owner: dadb
--

COPY public.exam (clinical_id, peritonitis, migratory_pain, lower_right_abd_pain, contralateral_rebound_tenderness, ipsilateral_rebound_tenderness, coughing_pain, psoas_sign, nausea, loss_of_appetite, body_temperature, dysuria, stool, visit_id) FROM stdin;
1	no	yes	yes	no	no	yes	positive	yes	yes	38.1	no	normal	1
2	no	yes	yes	no	yes	no	negative	no	yes	36.1	no	normal	2
3	no	yes	yes	no	yes	yes	positive	yes	yes	36	no	normal	3
4	no	yes	yes	yes	yes	yes	positive	yes	yes	36.6	no	normal	4
5	no	yes	yes	no	yes	no	positive	no	yes	36	no	normal	5
6	no	yes	yes	yes	yes	yes	positive	yes	yes	37.3	no	normal	6
7	no	yes	yes	no	yes	yes	positive	yes	yes	36.3	no	normal	7
8	no	yes	yes	yes	yes	yes	positive	yes	yes	36.8	no	normal	8
9	no	yes	yes	no	yes	no	positive	no	yes	37.4	no	normal	9
10	no	yes	yes	no	yes	yes	positive	yes	yes	38.3	no	normal	10
\.


--
-- Data for Name: lab; Type: TABLE DATA; Schema: public; Owner: dadb
--

COPY public.lab (lab_id, neutrophil_percentage, wbc_count, neutrophilia, ketones_in_urine, rdw, hemoglobin, rbc_count, rbc_in_urine, thrombocyte_count, wbc_in_urine, visit_id) FROM stdin;
1	73.7	6.8	no	+++	14.1	12.4	267	no	5.19	no	1
2	57.9	6.5	no	no	14.2	12.8	271	no	4.93	no	2
3	84.1	13.4	yes	+	13.6	12.4	250	no	4.96	no	3
4	53.3	6.6	no	+	15.8	11.9	254	no	5.31	no	4
5	53	7.4	no	no	12.9	12.3	266	no	4.48	no	5
6	56	10.7	no	++	12.2	11.8	284	+	4.15	no	6
7	84.5	16.1	yes	no	13.2	11.5	332	no	4.55	no	7
8	49.8	6.4	no	no	12.5	11.9	286	no	4.51	no	8
9	73.2	11	no	no	13.4	13.4	279	no	4.67	no	9
10	73.5	16.7	no	no	13.3	11.8	239	no	4.83	no	10
\.


--
-- Data for Name: patient; Type: TABLE DATA; Schema: public; Owner: dadb
--

COPY public.patient (patient_id, f_name, l_name, age, gender) FROM stdin;
1	Alice	Brown	13.39	female
2	Bob	Green	17.24	female
3	Charlie	Johnson	10.58	female
4	David	Brown	16.66	male
5	Emily	Davis	13.26	female
6	Fiona	Garcia	8.69	female
7	Grace	Lee	10.51	female
8	Hannah	Clark	13.54	female
9	Isabella	Martinez	10.55	male
10	Jack	Rodriguez	10.36	female
\.


--
-- Data for Name: physician; Type: TABLE DATA; Schema: public; Owner: dadb
--

COPY public.physician (physician_id, f_name, l_name, email, password) FROM stdin;
1	John	Smith	john.smith@hospital.com	123456
2	Emma	Davis	emma.davis@hospital.com	123456
\.


--
-- Data for Name: visit; Type: TABLE DATA; Schema: public; Owner: dadb
--

COPY public.visit (visit_id, patient_id, physician_id) FROM stdin;
1	1	1
2	2	2
3	3	1
4	4	1
5	5	1
6	6	1
7	7	1
8	8	1
9	9	1
10	10	1
\.


--
-- Data for Name: vital_sign; Type: TABLE DATA; Schema: public; Owner: dadb
--

COPY public.vital_sign (demographic_id, height, weight, bmi, visit_id) FROM stdin;
1	153	40.7	17.5	1
2	163	88	33.1	2
3	152	43	18.6	3
4	174	65	21.5	4
5	160	62	24.2	5
6	139	31	16	6
7	150	40	17.8	7
8	166	48	17.4	8
9	141	36	18.1	9
10	138	31	16.3	10
\.


--
-- Name: exam clinical_pkey; Type: CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.exam
    ADD CONSTRAINT clinical_pkey PRIMARY KEY (clinical_id);


--
-- Name: vital_sign demographics_pkey; Type: CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.vital_sign
    ADD CONSTRAINT demographics_pkey PRIMARY KEY (demographic_id);


--
-- Name: diagnosis diagnosis_pkey; Type: CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.diagnosis
    ADD CONSTRAINT diagnosis_pkey PRIMARY KEY (diagnosis_id);


--
-- Name: lab lab_pkey; Type: CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.lab
    ADD CONSTRAINT lab_pkey PRIMARY KEY (lab_id);


--
-- Name: patient patient_pkey; Type: CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.patient
    ADD CONSTRAINT patient_pkey PRIMARY KEY (patient_id);


--
-- Name: physician physician_pkey; Type: CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.physician
    ADD CONSTRAINT physician_pkey PRIMARY KEY (physician_id);


--
-- Name: visit visit_pkey; Type: CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT visit_pkey PRIMARY KEY (visit_id);


--
-- Name: exam clinical_visit_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.exam
    ADD CONSTRAINT clinical_visit_id_fkey FOREIGN KEY (visit_id) REFERENCES public.visit(visit_id);


--
-- Name: vital_sign demographics_visit_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.vital_sign
    ADD CONSTRAINT demographics_visit_id_fkey FOREIGN KEY (visit_id) REFERENCES public.visit(visit_id);


--
-- Name: diagnosis diagnosis_visit_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.diagnosis
    ADD CONSTRAINT diagnosis_visit_id_fkey FOREIGN KEY (visit_id) REFERENCES public.visit(visit_id);


--
-- Name: lab lab_visit_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.lab
    ADD CONSTRAINT lab_visit_id_fkey FOREIGN KEY (visit_id) REFERENCES public.visit(visit_id);


--
-- Name: visit visit_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT visit_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patient(patient_id);


--
-- Name: visit visit_physician_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dadb
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT visit_physician_id_fkey FOREIGN KEY (physician_id) REFERENCES public.physician(physician_id);


--
-- PostgreSQL database dump complete
--

