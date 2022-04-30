import React from "react";
import {
  ComposedChart,
  Line,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend
} from "recharts";

const data = [
  {
    name: "비스킷",
    fat: 4.0,
    mean: 4.76,
  },
  {
    name: "크래커",
    fat: 1.0,
    mean: 4.76,
  },
  {
    name: "채썬 밀 비스킷",
    fat: 1.0,
    mean: 4.76
  },
  {
    name: "와플",
    fat: 9.0,
    mean: 4.76
  },
  {
    name: "애플 베티",
    fat: 4.0,
    mean: 4.76
  },
  {
    name: "빵 푸딩",
    fat: 12.0,
    mean: 4.76
  },
  {
    name: "케이크",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "초콜릿 퍼지",
    fat: 14.0,
    mean: 4.76
  },
  {
    name: "컵 케이크",
    fat: 3.0,
    mean: 4.76
  },
  {
    name: "과일 케이크",
    fat: 4.0,
    mean: 4.76
  },
  {
    name: "생강 빵",
    fat: 7.0,
    mean: 4.76
  },
  {
    name: "스폰지 케이크",
    fat: 2.0,
    mean: 4.76
  },
  {
    name: "사탕",
    fat: 3.0,
    mean: 4.76
  },
  {
    name: "초콜릿 크림",
    fat: 4.0,
    mean: 4.76
  },
  {
    name: "퍼지",
    fat: 12.0,
    mean: 4.76
  },
  {
    name: "단단한 사탕",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "마쉬 멜 로우",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "밀크 초콜릿",
    fat: 6.0,
    mean: 4.76
  },
  {
    name: "초콜릿 시럽",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "도너츠",
    fat: 7.0,
    mean: 4.76
  },
  {
    name: "꿀",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "빙과",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "보존",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "젤리",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "당밀",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "캔디 시럽",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "9호 파이",
    fat: 13.0,
    mean: 4.76
  },
  {
    name: "체리 파이",
    fat: 13.0,
    mean: 4.76
  },
  {
    name: "레몬 머랭",
    fat: 12.0,
    mean: 4.76
  },
  {
    name: "갈아 놓은 고기",
    fat: 9.0,
    mean: 4.76
  },
  {
    name: "호박 파이",
    fat: 12.0,
    mean: 4.76
  },
  {
    name: "설탕 3 티스푼",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "시럽",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "타피오카 크림 푸딩",
    fat: 10.0,
    mean: 4.76
  },
];

export default function FatDesserts() {
  return (
    <ComposedChart
      width={500}
      height={400}
      data={data}
      margin={{
        top: 20,
        right: 20,
        bottom: 20,
        left: 20
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" scale="band" />
      <YAxis label={{ value: "ww", angle: -90, position: "insideLeft" }} />
      <Tooltip />
      <Legend />
      <Bar dataKey="fat" barSize={7} fill="#F77F00" />
      <Line type="monotone" dot={false} dataKey="mean" stroke="#2D00F7" />
    </ComposedChart>
  );
}
