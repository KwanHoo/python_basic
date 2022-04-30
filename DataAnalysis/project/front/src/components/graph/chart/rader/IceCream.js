import React from "react";
import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis
} from "recharts";

const data = [
  {
    subject: "carbs",
    A: 29,
    B: 110,
    fullMark: 150
  },
  {
    subject: "fat",
    A: 18,
    B: 130,
    fullMark: 150
  },
  {
    subject: "satFat",
    A: 16,
    B: 130,
    fullMark: 150
  },
  {
    subject: "fiber",
    A: 0,
    B: 100,
    fullMark: 150
  },
  {
    subject: "protein",
    A: 6,
    B: 90,
    fullMark: 150
  },

];

export default function IceCream() {
  return (
    <RadarChart
      cx={300}
      cy={250}
      outerRadius={150}
      width={500}
      height={500}
      data={data}
    >
      <PolarGrid />
      <PolarAngleAxis dataKey="subject" />
      <PolarRadiusAxis />
      <Radar
        name="아이스크림"
        dataKey="A"
        stroke="#8884d8"
        fill="#8884d8"
        fillOpacity={0.6}
      />
    </RadarChart>
  );
}
